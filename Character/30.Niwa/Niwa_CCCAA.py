import Function as f;

var x = 0;
var y = 0;

var d = 75;

function main(cp)
{
   MoveUnit(All, "40 + 3n Zeratul", cp, "Anywhere", "[Skill]HoldPosition");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {

      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            CreateUnit(1, "40 + 3n Zeratul", "[Skill]Hallu_Bozo", cp);

            f.Table_Sin(cp, 22, d);
            f.Table_Cos(cp, 22, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         if (f.loop[cp] == 2)
         {
            f.Table_Sin(cp, 67, d);
            f.Table_Cos(cp, 67, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.Table_Sin(cp, 22, 2 * d);
            f.Table_Cos(cp, 22, 2 * d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.Table_Sin(cp, 67, 2 * d);
            f.Table_Cos(cp, 67, 2 * d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
            f.SquareShape(cp, 1, "Protoss Dark Archon", x, y);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 6)
         {
            f.Table_Sin(cp, 67, d);
            f.Table_Cos(cp, 67, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Guardian", x, y);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         }
         if (f.loop[cp] == 8)
         {
            f.Table_Sin(cp, 22, d);
            f.Table_Cos(cp, 22, d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "Kakaru (Twilight)", x, y);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.Table_Sin(cp, 67, 2 * d);
            f.Table_Cos(cp, 67, 2 * d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", x, y);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.Table_Sin(cp, 22, 2 * d);
            f.Table_Cos(cp, 22, 2 * d);

            x = f.CosAngle[cp];
            y = f.SinAngle[cp];

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", x, y);
            f.SquareShape(cp, 1, "Protoss Dark Archon", x, y);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 15)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (Bring(cp, AtLeast, 1, "Protoss Dark Templar", "Anywhere"))
         {
            f.MoveLoc("Protoss Dark Templar", cp, 0, 0);
            RemoveUnitAt(1, "Protoss Dark Templar", "Anywhere", cp);
            f.SkillUnit(cp, 1, "40 + 1n Drone");
            if (f.loop[cp] % 2 == 0)
            {
               f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               f.SkillUnit(cp, 1, "40 + 1n Guardian");
            }
            if (f.loop[cp] % 2 == 1)
            {
               f.SkillUnit(cp, 1, "Kakaru (Twilight)");
               f.SkillUnit(cp, 1, "40 + 1n Zealot");
            }

            f.SkillUnitWithProperty(cp, 1, "40 + 1n Lurker", 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "40 + 1n Drone", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            MoveUnit(All, "40 + 1n Lurker", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);
         }
         
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 30)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", cp);
         KillUnitAt(All, "Unclean One (Defiler)", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}