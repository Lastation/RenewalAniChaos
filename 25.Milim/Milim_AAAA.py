import Function as f;

const s = StringBuffer();

function main(cp)
{
   MoveLocation("25.Milim_Bozo", f.heroID[cp], cp, "Anywhere");

   f.BanReturn(cp);
   f.HoldPosition(cp);

   ModifyUnitShields(All, f.heroID[cp], cp, "Anywhere", 1);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("Recall - MilimUlt", Set);
            SetDeaths(cp, SetTo, 1, " `ShieldRecharge");

            f.SkillWait(cp, 720);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 5)
         {
            f.NxNSquareShape(cp, 1, "Protoss Observer", 11, 75);
            f.NxNSquareShape(cp, 1, "60 + 1n Archon", 11, 75);

            KillUnitAt(All, "Protoss Observer", "Anywhere", cp);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 5)
         {
            f.NxNSquareShape(cp, 1, " Unit. Hoffnung 25000", 11, 75);
            f.NxNSquareShape(cp, 1, "40 + 1n Guardian", 11, 75);

            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SkillWait(cp, 480);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 6)
         {
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 720);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 2160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] == 0)
         {         
            f.SkillWait(cp, 1280);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            f.Voice_Routine(cp, 8);
            f.SkillWait(cp, 80);
            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] == 0)
         {         
            if (cp < 3)
            {
               GiveUnits(All, "80 + 1n Artanis", cp, "Anywhere", P7);
               GiveUnits(All, "80 + 1n Mutalisk", cp, "Anywhere", P7);
               GiveUnits(All, "80 + 1n Tom Kazansky", cp, "Anywhere", P7);
            }
            else if (cp >= 3)
            {
               GiveUnits(All, "80 + 1n Artanis", cp, "Anywhere", P8);
               GiveUnits(All, "80 + 1n Mutalisk", cp, "Anywhere", P8);
               GiveUnits(All, "80 + 1n Tom Kazansky", cp, "Anywhere", P8);
            }
            SetSwitch("JunkYardDog", Set);

            f.SkillWait(cp, 800);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            if (cp < 3)
            {
               GiveUnits(All, "80 + 1n Artanis", P7, "Anywhere", cp);
               GiveUnits(All, "80 + 1n Mutalisk", P7, "Anywhere", cp);
               GiveUnits(All, "80 + 1n Tom Kazansky", P7, "Anywhere", cp);
            }
            else if (cp >= 3)
            {
               GiveUnits(All, "80 + 1n Artanis", P8, "Anywhere", cp);
               GiveUnits(All, "80 + 1n Mutalisk", P8, "Anywhere", cp);
               GiveUnits(All, "80 + 1n Tom Kazansky", P8, "Anywhere", cp);
            }
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);
            Order("80 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

            SetSwitch("JunkYardDog", Clear);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 12)
         {         
            if (f.loop[cp] % 3 == 0)
            {
               f.EdgeShape(cp, 1, "40 + 1n Mojo", 0, 11, 30 * f.loop[cp]);
               f.EdgeShape(cp, 1, "60 + 1n Archon", 0, 11, 30 * f.loop[cp]);
            }
            else if (f.loop[cp] % 3 == 1)
            {
               f.EdgeShape(cp, 1, "40 + 1n Wraith", 0, 11, 30 * f.loop[cp]);
               f.EdgeShape(cp, 1, "Protoss Dark Archon", 0, 11, 30 * f.loop[cp]);
            }     
            else if (f.loop[cp] % 3 == 2)
            {
               f.EdgeShape(cp, 1, "40 + 1n Mutalisk", 0, 11, 30 * f.loop[cp]);
               f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 0, 11, 30 * f.loop[cp]);
            }     
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
            Order("40 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 160);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 12)
         {         
            f.SkillWait(cp, 1920);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 13)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }


      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] < 9)
         {         
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 9, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 320);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 9)
         {         
            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 6)
      {
         SetSwitch("UiltimateSwitch", Clear);
         SetSwitch("Recall - MilimUlt", Clear);
         KillUnitAt(All, "80 + 1n Artanis", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

         f.SkillEnd(cp);
      }
   }
   if (f.delayB[cp] == 0)
   {
      if (f.count[cp] == 1)
      {
         if (f.loopB[cp] == 9) f.loopB[cp] = 0;
         if (f.loopB[cp] < 9)
         {
            f.Table_Sin(cp, 10 * f.loopB[cp], 300);
            f.Table_Cos(cp, 10 * f.loopB[cp], 300);

            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "80 + 1n Artanis", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Move, f.location[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            RemoveUnitAt(All, "80 + 1n Artanis", f.location[cp], cp);
            RemoveUnitAt(All, "80 + 1n Mutalisk", f.location[cp], cp);
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", f.location[cp], cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
      }
      else if (f.count[cp] <= 3)
      {
         if (f.loopB[cp] == 9) f.loopB[cp] = 0;
         if (f.loopB[cp] < 9)
         {
            f.Table_Sin(cp, 10 * f.loopB[cp], 300);
            f.Table_Cos(cp, 10 * f.loopB[cp], 300);

            f.SquareShape(cp, 1, "Protoss Dark Archon", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "80 + 1n Artanis", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 10 * f.loopB[cp] + 30, 300);
            f.Table_Cos(cp, 10 * f.loopB[cp] + 30, 300);

            f.SquareShape(cp, 1, " Unit. Hoffnung 25000", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "80 + 1n Tom Kazansky", f.CosAngle[cp], f.SinAngle[cp]);

            f.Table_Sin(cp, 10 * f.loopB[cp] + 60, 300);
            f.Table_Cos(cp, 10 * f.loopB[cp] + 60, 300);

            f.SquareShape(cp, 1, "50 + 1n Tank", f.CosAngle[cp], f.SinAngle[cp]);
            f.SquareShape(cp, 1, "80 + 1n Mutalisk", f.CosAngle[cp], f.SinAngle[cp]);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Artanis", cp, "Anywhere", Move, f.location[cp]);
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Move, f.location[cp]);
            Order("80 + 1n Mutalisk", cp, "Anywhere", Move, f.location[cp]);

            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            RemoveUnitAt(All, "80 + 1n Artanis", f.location[cp], cp);
            RemoveUnitAt(All, "80 + 1n Mutalisk", f.location[cp], cp);
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", f.location[cp], cp);

            f.SkillWaitB(cp, 160);

            f.loopB[cp] += 1;
         }
      }
      else if (f.count[cp] <= 5)
      {
         MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         RemoveUnitAt(All, "80 + 1n Artanis", f.location[cp], cp);
         RemoveUnitAt(All, "80 + 1n Mutalisk", f.location[cp], cp);
         RemoveUnitAt(All, "80 + 1n Tom Kazansky", f.location[cp], cp);
         Order("80 + 1n Artanis", cp, "Anywhere", Attack, f.location[cp]);
         Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);
         Order("80 + 1n Mutalisk", cp, "Anywhere", Attack, f.location[cp]);

         f.SkillWaitB(cp, 160);
      }

   }
   if (f.delayC[cp] == 0)
   {
      if (f.count[cp] == 1)
      {
         if (f.loopC[cp] >= 3) f.loopC[cp] = 0;
         if (f.loopC[cp] < 3)
         {
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 9, 75);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
      }
      else if (f.count[cp] <= 3)
      {
         if (f.loopC[cp] >= 2) f.loopC[cp] = 0;
         if (f.loopC[cp] == 0)
         {
            f.NxNSquareShape(cp, 1, "Protoss Dark Archon", 9, 75);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
         else if (f.loopC[cp] == 1)
         {
            f.NxNSquareShape(cp, 1, "50 + 1n Tank", 9, 75);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWaitC(cp, 320);

            f.loopC[cp] += 1;
         }
      }
   }



}