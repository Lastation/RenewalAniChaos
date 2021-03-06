import Function as f;

function EdgeShapeAt(cp : TrgPlayer, count, Unit : TrgUnit, degree, n, interval, x, y);

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);
   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            SetSwitch("JunkYardDog - Niwa", Set);
            SetSwitch("Recall - Niwa", Set);
         }

         GiveUnits(All, "40 + 1n Wraith", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mutalisk", P7, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Wraith", P8, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mojo", P8, "Anywhere", P12);
         GiveUnits(All, "40 + 1n Mutalisk", P8, "Anywhere", P12);
         if (f.loop[cp] < 56)
         {
            GiveUnits(All, "Kakaru (Twilight)", P7, "Anywhere", P12);
            GiveUnits(All, "Kakaru (Twilight)", P8, "Anywhere", P12);  
         }
         if (f.loop[cp] >= 56)
         {
            GiveUnits(All, "Kakaru (Twilight)", P7, "Anywhere", cp);
            GiveUnits(All, "Kakaru (Twilight)", P8, "Anywhere", cp);
            GiveUnits(All, "Kakaru (Twilight)", P12, "Anywhere", cp);  
         }

         if (Bring(cp, AtLeast, 1, "60 + 1n Siege", "Anywhere"))
         {
            for (var i = 0; i < 3; i++)
            {
               f.MoveLoc("60 + 1n Siege", cp, 0, 0);
               RemoveUnitAt(1, "60 + 1n Siege", "Anywhere", cp);
               if (i % 3 == 0) 
               {
                  f.SkillUnit(cp, 1, "40 + 1n Wraith");
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, "50 + 1n Tank");
               }
               else if (i % 3 == 1)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Mutalisk");
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               }
               else if (i % 3 == 2)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Mojo");
                  f.SkillUnit(cp, 1, "Kakaru (Twilight)");
                  f.SkillUnit(cp, 1, "60 + 1n Archon");
               }

            }
         }
         if (Bring(cp, AtLeast, 1, "60 + 1n Hydralisk", "Anywhere"))
         {
            for (var i = 0; i < 3; i++)
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
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);


         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         Order("Kakaru (Twilight)", cp, "Anywhere", Move, f.location[cp]);


         if (cp < 3)
         {
            GiveUnits(All, "40 + 1n Wraith", cp, f.location[cp], P7);
            GiveUnits(All, "40 + 1n Mojo", cp, f.location[cp], P7);
            GiveUnits(All, "40 + 1n Mutalisk", cp, f.location[cp], P7);
            if (f.loop[cp] < 56)
               GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P7);

            GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", P7);
            GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
            GiveUnits(All, "40 + 1n Mutalisk", P12, "Anywhere", P7);
            if (f.loop[cp] < 56)
               GiveUnits(All, "Kakaru (Twilight)", P12, "Anywhere", P7);

         }
         else if (cp >= 3)
         {
            GiveUnits(All, "40 + 1n Wraith", cp, f.location[cp], P8);
            GiveUnits(All, "40 + 1n Mojo", cp, f.location[cp], P8);
            GiveUnits(All, "40 + 1n Mutalisk", cp, f.location[cp], P8);
            if (f.loop[cp] < 56)
               GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P8);

            GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", P8);
            GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P8);
            GiveUnits(All, "40 + 1n Mutalisk", P12, "Anywhere", P8);
            if (f.loop[cp] < 56)
               GiveUnits(All, "Kakaru (Twilight)", P12, "Anywhere", P8);
         }

         for (var i = 0; i < 18; i++)
         {
            f.Table_Sin(cp, 20 * i, 400);
            f.Table_Cos(cp, 20 * i, 400);

            MoveLocation("30.Niwa_Bozo", f.heroID[cp], cp, "Anywhere");
            addloc("30.Niwa_Bozo", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 20 * (i + 4), 430);
            f.Table_Cos(cp, 20 * (i + 4), 430);

            f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
            Order("Kakaru (Twilight)", P7, "30.Niwa_Bozo", Move, f.location[cp]);
            Order("Kakaru (Twilight)", P8, "30.Niwa_Bozo", Move, f.location[cp]);

            f.Table_Sin(cp, 20 * (i + 4), 400);
            f.Table_Cos(cp, 20 * (i + 4), 400);

            f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
            Order("40 + 1n Mutalisk", P8, "30.Niwa_Bozo", Move, f.location[cp]);
            Order("40 + 1n Mutalisk", P7, "30.Niwa_Bozo", Move, f.location[cp]);

            f.Table_Sin(cp, 20 * (i + 4), 370);
            f.Table_Cos(cp, 20 * (i + 4), 370);

            f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
            Order("40 + 1n Wraith", P7, "30.Niwa_Bozo", Move, f.location[cp]);
            Order("40 + 1n Wraith", P8, "30.Niwa_Bozo", Move, f.location[cp]);

            f.Table_Sin(cp, 20 * (i + 4), 340);
            f.Table_Cos(cp, 20 * (i + 4), 340);

            f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
            Order("40 + 1n Mojo", P7, "30.Niwa_Bozo", Move, f.location[cp]);
            Order("40 + 1n Mojo", P8, "30.Niwa_Bozo", Move, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 79)
         {
            f.Voice_Routine(cp, 4);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            if (cp < 3)
            {
               GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", P7);
               GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
               GiveUnits(All, "40 + 1n Mutalisk", P12, "Anywhere", P7);

            }
            else if (cp >= 3)
            {
               GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", P8);
               GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P8);
               GiveUnits(All, "40 + 1n Mutalisk", P12, "Anywhere", P8);

            }
         }
         if (f.loop[cp] == 10)
         {
            f.Voice_Routine(cp, 5);
         }

         if (f.loop[cp] < 25)
         {

            if (cp < 3)
            {
               GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P7);
            }
            else if (cp >= 3)
            {
               GiveUnits(All, "Kakaru (Twilight)", cp, f.location[cp], P8);
            }
         }

         if (f.loop[cp] < 25)
         {
            for (var i = 0; i < 18; i++)
            {
               f.Table_Sin(cp, 20 * i, 400);
               f.Table_Cos(cp, 20 * i, 400);

               MoveLocation("30.Niwa_Bozo", f.heroID[cp], cp, "Anywhere");
               addloc("30.Niwa_Bozo", f.CosAngle[cp], f.SinAngle[cp]);

               f.Table_Sin(cp, 20 * (i + 4), 430);
               f.Table_Cos(cp, 20 * (i + 4), 430);

               f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
               Order("Kakaru (Twilight)", P7, "30.Niwa_Bozo", Move, f.location[cp]);
               Order("Kakaru (Twilight)", P8, "30.Niwa_Bozo", Move, f.location[cp]);

               f.Table_Sin(cp, 20 * (i + 4), 400);
               f.Table_Cos(cp, 20 * (i + 4), 400);

               f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
               Order("40 + 1n Mutalisk", P8, "30.Niwa_Bozo", Move, f.location[cp]);
               Order("40 + 1n Mutalisk", P7, "30.Niwa_Bozo", Move, f.location[cp]);

               f.Table_Sin(cp, 20 * (i + 4), 370);
               f.Table_Cos(cp, 20 * (i + 4), 370);

               f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
               Order("40 + 1n Wraith", P7, "30.Niwa_Bozo", Move, f.location[cp]);
               Order("40 + 1n Wraith", P8, "30.Niwa_Bozo", Move, f.location[cp]);

               f.Table_Sin(cp, 20 * (i + 4), 340);
               f.Table_Cos(cp, 20 * (i + 4), 340);

               f.MoveLoc(f.heroID[cp], cp, f.CosAngle[cp], f.SinAngle[cp]);
               Order("40 + 1n Mojo", P7, "30.Niwa_Bozo", Move, f.location[cp]);
               Order("40 + 1n Mojo", P8, "30.Niwa_Bozo", Move, f.location[cp]);
            }
         }
         if (f.loop[cp] == 25)
         {
            for (var i = 0; i < 2; i++)
            {
               f.Table_Sin(cp, 22 + 45 * i, 200);
               f.Table_Cos(cp, 22 + 45 * i, 200);

               var x = f.CosAngle[cp];
               var y = f.SinAngle[cp];

               EdgeShapeAt(cp, 1, "40 + 1n Gantrithor", 0, 2, 75, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 2, 75, x, y);
            }
            GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", cp);
            GiveUnits(All, "40 + 1n Mojo", P8, "Anywhere", cp);
            GiveUnits(All, "Kakaru (Twilight)", P7, "Anywhere", cp);
            GiveUnits(All, "Kakaru (Twilight)", P8, "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);

         }
         if (f.loop[cp] == 27)
         {
            GiveUnits(All, "40 + 1n Wraith", P7, "Anywhere", cp);
            GiveUnits(All, "40 + 1n Wraith", P8, "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 29)
         {
            for (var i = 0; i < 4; i++)
            {
               f.Table_Sin(cp, 22 + 22 * i, 400);
               f.Table_Cos(cp, 22 + 22 * i, 400);

               var x = f.CosAngle[cp];
               var y = f.SinAngle[cp];

               EdgeShapeAt(cp, 1, "40 + 1n Gantrithor", 0, 2, 75, x, y);
               EdgeShapeAt(cp, 1, "60 + 1n Archon", 0, 2, 75, x, y);
            }


            GiveUnits(All, "40 + 1n Mutalisk", P7, "Anywhere", cp);
            GiveUnits(All, "40 + 1n Mutalisk", P8, "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
         }


         if (f.loop[cp] > 46)
         {
            if (Bring(cp, AtLeast, 1, "Kakaru (Twilight)", "Anywhere"))
            {
               for (var i = 0; i < 6; i++)
               {
                  f.MoveLoc("Kakaru (Twilight)", cp, 0, 0);
                  RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
                  if (i % 3 == 0) 
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Drone");
                     f.SkillUnit(cp, 1, "50 + 1n Tank");
                  }
                  else if (i % 3 == 1)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Drone");
                     f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
                  }
                  else if (i % 3 == 2)
                  {
                     f.SkillUnit(cp, 1, "40 + 1n Drone");
                     f.SkillUnit(cp, 1, "40 + 1n Guardian");
                  }
               }

               MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
               Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

            }
         }
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

         RemoveUnitAt(All, "40 + 1n Drone", "[Skill]Unit_Wait_ALL", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 81)
         {

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         if (Bring(cp, AtLeast, 1, "40 + 1n Wraith", "Anywhere"))
         {
            for (var i = 0; i < 2; i++)
            {
               f.MoveLoc("40 + 1n Wraith", cp, 0, 0);
               RemoveUnitAt(1, "40 + 1n Wraith", "Anywhere", cp);
               f.SkillUnit(cp, 1, "80 + 1n Tom Kazansky");
               f.SkillUnit(cp, 1, "50 + 1n Tank");
            }
         }
         if (Bring(cp, AtLeast, 1, "40 + 1n Mojo", "Anywhere"))
         {
            for (var i = 0; i < 2; i++)
            {
               f.MoveLoc("40 + 1n Mojo", cp, 0, 0);
               RemoveUnitAt(1, "40 + 1n Mojo", "Anywhere", cp);
               f.SkillUnit(cp, 1, "80 + 1n Artanis");
               f.SkillUnit(cp, 1, "60 + 1n Archon");
            }
         }
         if (Bring(cp, AtLeast, 1, "40 + 1n Mutalisk", "Anywhere"))
         {
            for (var i = 0; i < 2; i++)
            {
               f.MoveLoc("40 + 1n Mutalisk", cp, 0, 0);
               RemoveUnitAt(1, "40 + 1n Mutalisk", "Anywhere", cp);
               f.SkillUnit(cp, 1, "80 + 1n Mutalisk");
               f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
            }
         }

         KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
         KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);

         if (Bring(cp, AtLeast, 1, "Kakaru (Twilight)", "Anywhere"))
         {
            for (var i = 0; i < 6; i++)
            {
               f.MoveLoc("Kakaru (Twilight)", cp, 0, 0);
               RemoveUnitAt(1, "Kakaru (Twilight)", "Anywhere", cp);
               if (i % 3 == 0) 
               {
                  f.SkillUnit(cp, 1, "40 + 1n Drone");
                  f.SkillUnit(cp, 1, "50 + 1n Tank");
               }
               else if (i % 3 == 1)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Drone");
                  f.SkillUnit(cp, 1, " Unit. Hoffnung 25000");
               }
               else if (i % 3 == 2)
               {
                  f.SkillUnit(cp, 1, "40 + 1n Drone");
                  f.SkillUnit(cp, 1, "40 + 1n Guardian");
               }

            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Drone", cp, "Anywhere", Attack, f.location[cp]);

         }
         RemoveUnitAt(All, "40 + 1n Drone", "[Skill]Unit_Wait_ALL", cp);

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 51)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", cp);

         SetSwitch("UiltimateSwitch", Clear);
         SetSwitch("Recall - Niwa", Clear);
         SetSwitch("JunkYardDog - Niwa", Clear);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");
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
}

