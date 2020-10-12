import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("JunkYardDog - Niwa", Set);
            SetSwitch("Recall - Niwa", Set);
         }

         GiveUnits(All, "40 + 1n Wraith", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mutalisk", P7, "Anywhere", P12);
         GiveUnits(All, "Kakaru (Twilight)", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Wraith", P8, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mojo", P8, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mutalisk", P8, "Anywhere", P12);
         GiveUnits(All, "Kakaru (Twilight)", P8, "Anywhere", P12);

         if (Bring(cp, AtLeast, 1, "60 + 1n Siege", "Anywhere"))
         {
            for (var i = 0; i < 6; i++)
            {
               f.MoveLoc("60 + 1n Siege", cp, 0, 0);
               RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", cp);
               if (i % 3 == 0) 
               {
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, "50 + 1n Tank");
               }
               else if (i % 3 == 1)
               {
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               }
               else if (i % 3 == 2)
               {
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }

            }
         }
         if (Bring(cp, AtLeast, 1, "60 + 1n Hydralisk", "Anywhere"))
         {
            for (var i = 0; i < 6; i++)
            {
               f.MoveLoc("60 + 1n Hydralisk", cp, 0, 0);
               RemoveUnitAt(1, "60 + 1n Hydralisk", "Anywhere", cp);
               if (i % 3 == 0) 
               {
                  f.SkillUnit(cp, 1, "40 + 1n Wraith");
                  f.SkillUnit(cp, 1, "50 + 1n Tank");
               }
               else if (i % 3 == 1)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Mutalisk");
                  f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               }
               else if (i % 3 == 2)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Mojo");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }
            }
         }
         KillUnitAt(1, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(1, "Protoss Dark Archon", "Anywhere", cp);
         KillUnitAt(1, " Unit. Hoffnung 25000", "Anywhere", cp);

         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Wraith", cp, "Anywhere", Move, f.location[cp]);
         Order("40 + 1n Mojo", cp, "Anywhere", Move, f.location[cp]);
         Order("40 + 1n Mutalisk", cp, "Anywhere", Move, f.location[cp]);
         Order("Kakaru (Twilight)", cp, "Anywhere", Move, f.location[cp]);


         if (cp < 3)
         {
            GiveUnits(All, "40 + 1n Wraith", cp, f.location[cp], P7);
            GiveUnits(All, "40 + 1n Mojo", cp, f.location[cp], P7);
            GiveUnits(All, "40 + 1n Mutalisk", cp, f.location[cp], P7);
            GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P7);
         }
         else if (cp >= 3)
         {
            GiveUnits(All, "40 + 1n Wraith", cp, f.location[cp], P8);
            GiveUnits(All, "40 + 1n Mojo", cp, f.location[cp], P8);
            GiveUnits(All, "40 + 1n Mutalisk", cp, f.location[cp], P8);
            GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P8);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 64)
         {
            f.Voice_Routine(cp, 4);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         SetSwitch("UiltimateSwitch", Clear);
         f.SkillEnd(cp);
      }
   }

   MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
}

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y)
{
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, x, y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -x, -y);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, -y, x);
   f.EdgeShapeAt(cp, count, Unit, degree, n, interval, y, -x);

   f.DotShape(cp, count, Unit, x, y);
   f.DotShape(cp, count, Unit, -x, -y);
   f.DotShape(cp, count, Unit, -y, x);
   f.DotShape(cp, count, Unit, y, -x);
}

