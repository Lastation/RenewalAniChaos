import Function as f;
import Status as s;

var x = 0;
var y = 0;

var n = 0;
var max_loop = 0;

const offset = 32;
const unit = 32;
const bozo_location = 195;

var max_i = 0;

var v = 0;

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (cp < 3)
      max_i = 6;
   else if (cp >= 3)
      max_i = 3;

   for (var i = 0; i < 6; i++)
   {
      if (Bring(i, AtLeast, 1, f.heroID[i], "29.Ekidona_Bozo"))
      {
         s.SetEkidonaDebuff(i, f.count[cp] + 1);
      }
   }

   if (f.delay[cp] == 0 && f.count[cp] < 10)
   {
      MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");

      if (f.loop[cp] == 0)
      {
         v++;

         f.Voice_Routine(cp, 100 + v);

         if (f.count[cp] == 0)
         {
            SetSwitch("Recall - Ekidona", Set);
         }

         const location = EPD(0x58DC4C) + (f.location[cp] - 1) * 5;

         if (f.count[cp] == 0) { n = 20; max_loop = 225; }
         if (f.count[cp] == 1) { n = 40; max_loop = 225; }
         if (f.count[cp] == 2) { n = 60; max_loop = 305; }
         if (f.count[cp] == 3) { n = 80; max_loop = 175; }
         if (f.count[cp] == 4) { n = 100; max_loop = 235; }
         if (f.count[cp] == 5) { n = 120; max_loop = 225; }
         if (f.count[cp] == 6) { n = 140; max_loop = 145; }

         x = n * unit - offset; 
         y = n * unit - offset; 

         var x1 = dwread_epd(location + 0) - x;
         var x2 = dwread_epd(location + 2) + x;
         var y1 = dwread_epd(location + 1) + y;
         var y2 = dwread_epd(location + 3) - y;

         dwwrite_epd(EPD(0x58DC4C) + bozo_location * 5 + 0, x1);
         dwwrite_epd(EPD(0x58DC4C) + bozo_location * 5 + 2, x2);
         dwwrite_epd(EPD(0x58DC4C) + bozo_location * 5 + 1, y1);
         dwwrite_epd(EPD(0x58DC4C) + bozo_location * 5 + 3, y2);

         f.stb.print("x : ", x1, " y : ", y1);
         f.stb.print("x : ", dwread_epd(EPD(0x58DC4C) + bozo_location * 5 + 0), " y : ", dwread_epd(EPD(0x58DC4C) + bozo_location * 5 + 1));
         
         RemoveUnitAt(All, "Flame Red", "Anywhere", cp);

         f.EdgeShape(cp, 1, "Flame Red", 45, n / 2, 32 * n);

         RemoveUnitAt(All, "Flame Red", "[Skill]Unit_Wait_ALL", cp);
      }
      if (f.count[cp] > 0)
      {
         f.DotShape(cp, 1, "40 + 1n Guardian", 0, 0);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
      }
      if (f.count[cp] > 1)
      {
         f.Table_Sin(cp, 22 * f.loop[cp], 100);
         f.Table_Cos(cp, 22 * f.loop[cp], 100);

         var x = f.CosAngle[cp];
         var y = f.SinAngle[cp];

         f.DoubleShape(cp, 1, "Protoss Dark Archon", x, y);
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
      }
      if (f.count[cp] > 2)
      {
         f.Table_Sin(cp, 180 - 22 * (f.loop[cp] % 8), 200);
         f.Table_Cos(cp, 180 - 22 * (f.loop[cp] % 8), 200);

         var x = f.CosAngle[cp];
         var y = f.SinAngle[cp];

         f.DoubleShape(cp, 1, "Bengalaas (Jungle)", x, y);
         KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);
      }
      if (f.count[cp] > 3)
      {
         var i = (f.loop[cp] % 8);

         var x = 320 - 40 * i;
         var y = 40 * i;

         f.SquareShape(cp, 1, "50 + 1n Tank", x, y);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
      }
      if (f.count[cp] > 4)
      {
         var x = 250;
         var y = 0;

         f.SquareShape(cp, 4, "50 + 1n Tank", x, y);
         f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         x = 175;
         y = 175;

         f.SquareShape(cp, 4, "60 + 1n Archon", x, y);
         f.SquareShape(cp, 1, "40 + 1n Gantrithor", x, y);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
      }
      if (f.count[cp] > 5)
      {
         var x = 150;
         var y = 0;

         f.DoubleShape(cp, 8, "60 + 1n High Templar", x, y);
         f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

         x = 100;
         y = 100;

         f.DoubleShape(cp, 8, "60 + 1n High Templar", x, y);
         f.DoubleShape(cp, 1, "40 + 1n Guardian", x, y);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
      }

      f.SkillWait(cp, 80);

      f.loop[cp] += 1;

      if (f.loop[cp] >= max_loop)
      {
         if (Bring(cp, AtLeast, 1, "Protoss Corsair", "[Skill]UseSkill"))
         {
            KillUnitAt(1, "Protoss Corsair", "[Skill]UseSkill", cp);

            f.count[cp] += 1;
            f.loop[cp] = 0;   

            if (f.count[cp] == 7)
            {
               SetSwitch("Recall - Ekidona", Clear);
               SetDeaths(cp, SetTo, 360 * f.count[cp], " `UniqueCoolTime");

               v = 0;

               f.Voice_Routine(cp, 108);

               for (var i = 0; i < 6; i++)
               {
                  s.ekidonaDebuff[i] = 0;
               }

               RemoveUnitAt(All, "Flame Red", "Anywhere", cp);

               f.SkillEnd(cp);
            }
         }
         else
         {
            SetSwitch("Recall - Ekidona", Clear);
            SetDeaths(cp, SetTo, 360 * f.count[cp] + 360, " `UniqueCoolTime");

            v = 0;

            for (var i = 0; i < 6; i++)
            {
               s.ekidonaDebuff[i] = 0;
            }

            RemoveUnitAt(All, "Flame Red", "Anywhere", cp);

            f.SkillEnd(cp); 
         }
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}